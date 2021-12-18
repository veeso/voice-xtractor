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

from .audio import Audio, AudioSegment


class Track(Audio):
    """
    Track identifies an audio chunk taken from another `Audio`.
    The track has not a physical location and is considered to be a mutable audio entity
    """

    def __init__(self, audio: AudioSegment, name: str = None) -> None:
        super().__init__()
        self.__audio = audio
        self.__name = name
        self.__speech = ""

    @property
    def audio(self) -> AudioSegment:
        return self.__audio

    @property
    def slug(self) -> str:
        if self.__name:
            return self.__name
        else:
            return ""

    @property
    def speech(self) -> str:
        return self.__speech

    @speech.setter
    def speech(self, s: str) -> None:
        self.__speech = s

    def set_audio(self, audio: AudioSegment) -> None:
        self._audio = audio

    def set_name(self, name: str) -> None:
        """Set new name for `Track`"""
        self.__name = name
