#ifndef CONFIG_H
#define CONFIG_H

#define MBED_OS_SERIAL

// must have parameters
#define loopCycleTimeUs                            1000
#define CHANNELS_AVAILABLE_COUNT                      2
#define CHANNELS_REQUESTED_COUNT                      2
#define CHANNELS_UNREQUESTED_COUNT                    0
#define PARAMETER_COUNT                               1
#define SPECIAL_COMMANDS_COUNT                        2
#define BAUD_RATE                                 38400

// All requested channels
#define mR_testChannel                           (messageOutBuffer.channels[0])
#define mR_incChannel                            (messageOutBuffer.channels[1])

// All unrequested channels

// all parameters
#define mR_testParam                             (parameters[0])

// all special parameters
#define loopCycleTimeExceededByUs                (specialCommands[0])
#define serialTransmissionLag                    (specialCommands[1])


void microRayInit();
void microRayCommunicate();


#include <stdint.h>
typedef struct MessageOut
{
    uint32_t loopStartTime;
    uint32_t parameterNumber;
    float parameterValue;
    float channels[CHANNELS_REQUESTED_COUNT];
} MessageOut;

typedef struct MessageOutSerial
{
    uint8_t startByte;
    uint32_t loopStartTime;
    uint32_t parameterNumber;
    float parameterValue;
    float channels[CHANNELS_REQUESTED_COUNT];
    uint8_t stopByte;
} MessageOutSerial;


typedef struct MessageIn
{
    int32_t parameterNumber;
    float value;
} MessageIn;

// storage for channels
extern float unrequestedChannels[CHANNELS_UNREQUESTED_COUNT];

// storage for parameters, that could be set from the pc
extern float parameters[PARAMETER_COUNT];
extern float specialCommands[SPECIAL_COMMANDS_COUNT];

//extern MessageOutSerial messageOutBuffer;
extern MessageOut messageOutBuffer;
#endif