#include "microRay.h"

void prepareOutMessage();
void sendMessage();
void receiveMessage();

unsigned long lastTime = 0;

// storage for unrequested channels
float unrequestedChannels[CHANNELS_UNREQUESTED_COUNT];

// storage for parameters, that could be set from the pc
float parameters[PARAMETER_COUNT] = {0.0f};
float specialCommands[SPECIAL_COMMANDS_COUNT] = {0.0f};

int parameterSendCounter = 0;
int receivedBytesCount = 0;
int sendBytesCount = 0;

MessageOut messageOutBuffer;
MessageIn messageInBuffer;

void prepareOutMessage(unsigned long loopStartTime)
{
    // map rotating parameters
    // on each cycle, only one of the "controlled parameters" is send to the pc

    messageOutBuffer.loopStartTime = loopStartTime;

    if (parameterSendCounter < 0) {
        messageOutBuffer.parameterNumber = parameterSendCounter;
        //messageOutBuffer.parameterValue = parameters[requestedControlledParameters[parameterSendCounter]];
        messageOutBuffer.parameterValue = specialCommands[(parameterSendCounter + 1) * -1];
    }
    else {
        messageOutBuffer.parameterNumber = parameterSendCounter;
        //messageOutBuffer.parameterValue = parameters[requestedControlledParameters[parameterSendCounter]];
        messageOutBuffer.parameterValue = parameters[parameterSendCounter];
    }

    // increment the counter for sending the "slow parameters"
    parameterSendCounter += 1;
    if (parameterSendCounter >= PARAMETER_COUNT)
    {
        parameterSendCounter = SPECIAL_COMMANDS_COUNT * -1;
    }
}

void microRayCommunicate()
{
    sendMessage();
    receiveMessage();
}
void setInitialValues() {
    mR_testParam = 3.0f;
    loopCycleTimeExceededByUs = 0.0f;
    serialTransmissionLag = 0.0f;
}


#include <mbed.h>

void serialSendComplete(int events);

void receiveMessage();
void readIncomingBytesIntoBuffer();
void appendByteToBuffer(uint8_t inByte);
void shiftGivenPositionToBufferStart(int position);
int seekForFullMessage();
void extractMessage(int messageStartPosition);
void applyExtractedInMessage();


Serial mRserial(USBTX, USBRX, BAUD_RATE); // tx, rx

Timer dutyCycleTimer;
Timer debugTimer;
unsigned long timeOfLastSend = 0;
unsigned long timeOfLastCompletedMessage = 0;

DigitalOut redLed(LED3);
DigitalOut greenLed(LED1);

#define OUT_START_BYTE (char)7
#define OUT_STOP_BYTE (char)8

#define IN_MESSAGE_SIZE 8
#define IN_BUFFER_SIZE ((IN_MESSAGE_SIZE+2)*2)

#define IN_START_BYTE (char)7
#define IN_STOP_BYTE (char)8

event_callback_t serialEventWriteComplete;
int debugCounterSend = 0;
void serialSendComplete(int events) {
    mRserial.putc(OUT_STOP_BYTE);
    timeOfLastCompletedMessage = timeOfLastSend;
}

event_callback_t serialEventReceiveComplete;
uint8_t singleInBuffer = 0;
void serialReadComplete(int events) {
    appendByteToBuffer(singleInBuffer);

    // retrigger async receive of serial data
    mRserial.read(&singleInBuffer, 1, serialEventReceiveComplete);
}


void microRayInit() {
    setInitialValues();
    dutyCycleTimer.start();
    serialEventWriteComplete.attach(serialSendComplete);
    serialEventReceiveComplete.attach(serialReadComplete);
    mRserial.read(&singleInBuffer, 1, serialEventReceiveComplete);

    //mRserial.set_dma_usage_tx(1);
    //mRserial.set_dma_usage_rx(1);
}

int serialTransmissionLagCounter = 0;
void sendMessage() {

    prepareOutMessage((unsigned long)dutyCycleTimer.read_high_resolution_us());

    if(timeOfLastCompletedMessage == timeOfLastSend) {
        timeOfLastSend = (unsigned long)messageOutBuffer.loopStartTime;
        mRserial.putc(OUT_START_BYTE);
        mRserial.write((uint8_t *)&messageOutBuffer, sizeof(messageOutBuffer), serialEventWriteComplete, SERIAL_EVENT_TX_COMPLETE);
    }
    else {
        serialTransmissionLagCounter++;
        serialTransmissionLag = (float)serialTransmissionLagCounter;
        timeOfLastSend = (unsigned long)messageOutBuffer.loopStartTime;
    }
}

uint8_t rawMessageInBuffer[IN_BUFFER_SIZE];
uint8_t rawMessageInBufferTemp[IN_BUFFER_SIZE];
int16_t bufferPosition = 0;

void receiveMessage() {
    //readIncomingBytesIntoBuffer();
    int foundMessageStartPosition = seekForFullMessage();

    if(foundMessageStartPosition > -1) {
        extractMessage(foundMessageStartPosition);
        applyExtractedInMessage();
    }
}

void readIncomingBytesIntoBuffer() {
    appendByteToBuffer(singleInBuffer);
}

void appendByteToBuffer(uint8_t inByte) {
    // prevent buffer from overfilling
    // shift whole buffer one to the left to free last position
    if(bufferPosition >= IN_BUFFER_SIZE) {
        shiftGivenPositionToBufferStart(1);
    }
    rawMessageInBuffer[bufferPosition] = inByte;
    bufferPosition += 1;
}

void shiftGivenPositionToBufferStart(int position) {
    // copy and shift
    int i;
    for(i = position; i < bufferPosition; i++) {
        rawMessageInBufferTemp[i - position] = rawMessageInBuffer[i];
    }

    // actualize bufferPosition
    bufferPosition = bufferPosition - position;

    // copy back
    for(i = 0; i < bufferPosition; i++) {
        rawMessageInBuffer[i] = rawMessageInBufferTemp[i];
    }
}

int seekForFullMessage() {
    int i;
    for (i = 0; i < bufferPosition - IN_MESSAGE_SIZE; i++) {
        if (rawMessageInBuffer[i] == IN_START_BYTE) {
            int expectedStopBytePosition = i + IN_MESSAGE_SIZE + 1;
            if (rawMessageInBuffer[expectedStopBytePosition] == IN_STOP_BYTE) {
                return i;
            }
        }
    }
    return -1;
}

void extractMessage(int messageStartPosition) {
    memcpy(&messageInBuffer.parameterNumber, &rawMessageInBuffer[messageStartPosition + 1], 4);
    memcpy(&messageInBuffer.value, &rawMessageInBuffer[messageStartPosition + 1 + 4], 4);
    shiftGivenPositionToBufferStart(messageStartPosition + IN_MESSAGE_SIZE + 2);
}

void applyExtractedInMessage() {
    if (messageInBuffer.parameterNumber >= 0) {
        parameters[messageInBuffer.parameterNumber] = messageInBuffer.value;
    }
    else {
        specialCommands[(messageInBuffer.parameterNumber + 1) * -1] = messageInBuffer.value;
    }
}
