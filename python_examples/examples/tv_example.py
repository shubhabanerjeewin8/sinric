from time import sleep
from sinric import Sinric
import json

apiKey = 'Your Api Key'


def onSetPowerState(deviceId, value):
    # alexa, turn on tv ==> {"deviceId":"xx","action":"setPowerState","value":"ON"}
    print('setPowerState : value = ' + value)


def onSetMute(deviceId, value):
    # alexa, mute tv ==> {"deviceId":"xxx","action":"SetMute","value":{"mute":true}}
    tempValue = value['mute']
    if tempValue == True:
        print('Sound OFF')
    else:
        print('Sound ON')


def onAdjustVolume(deviceId, value):
    #   alexa, turn the volume down on tv by 20 ==> {"deviceId":"xxx","action":"AdjustVolume","value":{"volume":-20,"volumeDefault":false}}
    #  alexa, lower the volume on tv ==> {"deviceId":"xx","action":"AdjustVolume","value":{"volume":-10,"volumeDefault":true}}
    tempValue = value['volume']
    volumeDefault = value['volumeDefault']
    volume = int(tempValue)
    if volume < 0:
        print('Volume decreased by : ' + str(volume))
    else:
        print('Volume increased by : ' + str(volume))


def onChangeChannel(deviceId, value):
    # alexa, change channel to 200 on tv ==> {"deviceId":"xx","action":"ChangeChannel","value":{"channel":{},"channelMetadata":{"name":"CH9-200"}}}
    #  alexa, change channel to pbs on tv ==> {"deviceId":"xx","action":"ChangeChannel","value":{"channel":{},"channelMetadata":{"name":"pbs"}}}
    channel = value['channel']
    channelMetadata = value['channelMetadata']
    channelName = channelMetadata['name']
    print('Channel Changed to : ' + channelName)


def onSkipChannels(deviceId, value):
    # Alexa, next channel on tv ==>  {"deviceId":"xx","action":"SkipChannels","value":{"channelCount":1}}
    # Alexa may say Sorry, TV is not responding. but command works
    channelCount = value['channelCount']
    print('Channel Skipped by : ' + str(channelCount))


def onPreviosPlay(deviceId, value):
    # alexa, previous on tv ==> {"deviceId":"xx","action":"Previous","value":{}}
    # alexa, resume tv ==> {"deviceId":"xx","action":"Play","value":{}}
    # Alexa, pause tv ==> says I dont know that one...
    # for others check https://developer.amazon.com/docs/device-apis/alexa-playbackcontroller.html
    print(value)


def onSelectInput(deviceId, value):
    # alexa, change the input to hdmi ==> {"deviceId":"xx","action":"","value":{"input":"HDMI"}}
    Input = value['input']
    print('Selected : ' + Input)


def selectionAction(deviceId, action, value):
    if action == 'setPowerState':
        onSetPowerState(deviceId, value)
    elif action == 'SetMute':
        onSetMute(deviceId, value)
    elif action == 'AdjustVolume':
        onAdjustVolume(deviceId, value)
    elif action == 'ChangeChannel':
        onChangeChannel(deviceId, value)
    elif action == 'SkipChannels':
        onSkipChannels(deviceId, value)
    elif action == 'Previous' or action == 'Play':
        onPreviosPlay(deviceId, value)
    elif action == 'SelectInput':
        onSelectInput(deviceId, value)


if __name__ == '__main__':
    obj = Sinric(apiKey)
    while True:
        response = obj.initialize()
        data = json.loads(response)
        deviceId = data["deviceId"]
        action = data["action"]
        value = data["value"]
        selectionAction(deviceId, action, value)
        sleep(2)
