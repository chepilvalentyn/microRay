
#include <arduino.h>

void dumpOldMessages();
void copyOldMessageToIncomingBuffer();
void readIncomingBytesIntoBuffer();
void processMessage(int);
int findMessageAndProcess();
void storeForNextLoop(int);


void microRayInit() {
    setInitialValues();
    Serial.begin(BAUD_RATE);
}


void sendMessage() {
    prepareOutMessage(micros());
    //lastTime = micros();

    // Serial.write(messageOutBuffer.loopStartTime);
    // Serial.write(messageOutBuffer.lastLoopDuration);
    // Serial.write(messageOutBuffer.parameterNumber);
    // Serial.write(messageOutBuffer.parameterValue);
    //
    // int i = 0;
    // for (i; i < CHANNELS_REQUESTED_COUNT; i++) {
    //     Serial.write(messageOutBuffer.channels[i]);
    // }

    // check, if there is still data not send from the previous loop

    #ifdef SERIAL_TX_BUFFER_SIZE
        int bytesStillInBuffer = SERIAL_TX_BUFFER_SIZE - Serial.availableForWrite();
        if (bytesStillInBuffer > 1) {
            serialTransmissionLag = bytesStillInBuffer;
        }
    #endif
    Serial.write(7);
    Serial.write((byte *)&messageOutBuffer, sizeof(messageOutBuffer));
    Serial.write(8);

    // sendTimer = (float)(micros() - lastTime);
}



#define START_BYTE (char)7
#define STOP_BYTE (char)57
#define IN_MESSAGE_SIZE 8
#define BUFFER_SIZE ((IN_MESSAGE_SIZE+2)*2)

int16_t availableBytes = 0;

uint8_t remainderBuffer[BUFFER_SIZE];
int16_t bytesInRemainderBuffer = 0;

uint8_t dataToProcess[BUFFER_SIZE];
int16_t bytesInDataToProcess = 0;
int16_t dataToProcessPosition = 0;
int16_t searchPosition = 0;
int16_t lastPositionProcessed = -1;


void receiveMessage() {
    //lastTime = micros();
    //dumpOldMessages();
    copyOldMessageToIncomingBuffer();
    readIncomingBytesIntoBuffer();
    lastPositionProcessed = findMessageAndProcess();
    storeForNextLoop(lastPositionProcessed);
    // receiveTimer = (float)(micros() - lastTime);
}


void dumpOldMessages() {
    while(Serial.available() > BUFFER_SIZE) {
        Serial.read();
    }
}

void copyOldMessageToIncomingBuffer() {
    for (dataToProcessPosition = 0; dataToProcessPosition < bytesInRemainderBuffer; dataToProcessPosition++) {
        dataToProcess[dataToProcessPosition] = remainderBuffer[dataToProcessPosition];
        bytesInDataToProcess++;
    }
    bytesInRemainderBuffer = 0;
}

void readIncomingBytesIntoBuffer() {
//    dataToProcessPosition = bytesInDataToProcess;
    if (Serial.available() < (IN_MESSAGE_SIZE + 2)) {
        return;
    }
    while ((Serial.available() > 0) && (dataToProcessPosition < BUFFER_SIZE)) {
        dataToProcess[dataToProcessPosition] = Serial.read();
        dataToProcessPosition++;
        bytesInDataToProcess++;
    }
}

int findMessageAndProcess() {
    for (searchPosition = 0; searchPosition < bytesInDataToProcess; searchPosition++) {
        if (dataToProcess[searchPosition] == START_BYTE) {
            int expectedStopBytePosition = searchPosition + IN_MESSAGE_SIZE + 1;
            if (expectedStopBytePosition < BUFFER_SIZE) {
                if (dataToProcess[expectedStopBytePosition] == STOP_BYTE) {
                    processMessage(searchPosition + 1);
                    return expectedStopBytePosition;
                }
            }
            else {
                // do something meaningful
            }
        }
    }
    return -1;
}

void processMessage(int messageStartPosition) {
    memcpy(&messageInBuffer.parameterNumber, &dataToProcess[messageStartPosition], 4);
    memcpy(&messageInBuffer.value, &dataToProcess[messageStartPosition + 4], 4);
    if (messageInBuffer.parameterNumber >= 0) {
        parameters[messageInBuffer.parameterNumber] = messageInBuffer.value;
    }
    else {
        specialCommands[(messageInBuffer.parameterNumber + 1) * -1] = messageInBuffer.value;
    }

}



void storeForNextLoop(int lastPositionProcessed) {
    int positionResidueBuffer = 0;
    int positionInBuffer = lastPositionProcessed + 1;
    while (positionInBuffer < bytesInDataToProcess) {
        remainderBuffer[positionResidueBuffer] = dataToProcess[positionInBuffer];
        bytesInRemainderBuffer++;
        positionResidueBuffer++;
        positionInBuffer++;
    }
    bytesInDataToProcess = 0;
}
