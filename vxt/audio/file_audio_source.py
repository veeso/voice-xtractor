# VXT
# Developed by Christian Visintin
#
# MIT License
# Copyright (c) 2021 Christian Visintin
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from .audio_source import AudioSource, AudioSegment
from .error import AudioError


class FileAudioSource(AudioSource):
    """Defines an audio source located on a file system file"""

    def __init__(self, path: str) -> None:
        """
        Initialize a new AudioSource.
        Slug is a string which identifies the audio source uniquely,
        such as a file path or a device,
        while audio is the AudioSegment containing the audio.

        In case it fails to decode the audio file, raises a `AudioError`
        """
        audio = FileAudioSource.__open_audio_file(path)
        super().__init__(path, audio)

    @staticmethod
    def __open_audio_file(path: str) -> AudioSegment:
        """
        Open the audio file located at `path`.
        Raises `AudioError` in case of error
        """
        try:
            return AudioSegment.from_file(path)
        except Exception as e:
            raise AudioError(e)
