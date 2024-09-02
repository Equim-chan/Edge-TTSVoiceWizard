import base64
import argparse
from io import BytesIO
from tempfile import NamedTemporaryFile
from urllib.parse import unquote
from edge_tts import Communicate
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from pydub import AudioSegment

class SynthesizeHandler(RequestHandler):
    def initialize(self, voice):
        self.voice = voice

    async def get(self):
        # text = self.get_argument('text', '')
        text = unquote(self.request.query)

        communicate = Communicate(text, self.voice)
        with NamedTemporaryFile(delete_on_close=False) as f:
            async for message in communicate.stream():
                if message['type'] == 'audio':
                    f.write(message['data'])
            f.close()
            audio = AudioSegment.from_file(f.name)

        buf = BytesIO()
        audio.export(buf, format='wav')
        wav = buf.getvalue()

        encoded = base64.b64encode(wav)
        self.write(encoded)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--voice', help='voice for TTS. Default: en-US-AriaNeural', default='en-US-AriaNeural')
    args = parser.parse_args()

    app = Application([
        (r'/synthesize/', SynthesizeHandler, {'voice': args.voice}),
    ])
    app.listen(8124, '127.0.0.1')
    print('Server is running at http://127.0.0.1:8124')
    IOLoop.current().start()

if __name__ == '__main__':
    main()
