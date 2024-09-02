# Edge-TTSVoiceWizard
A very simple extension for [TTS Voice Wizard](https://github.com/VRCWizard/TTS-Voice-Wizard) based on [edge-tts](https://github.com/rany2/edge-tts).

## Usage
```shell
$ pip install -r requirements.txt
$ python main.py -v en-US-AriaNeural
```

Then select "Locally Hosted" under the "Text to Speech Mode" option in TTS Voice Wizard.

To check the list of voices, you can use the `edge-tts` CLI. More info [here](https://github.com/rany2/edge-tts?tab=readme-ov-file#usage).

```shell
$ edge-tts --list-voices
```
