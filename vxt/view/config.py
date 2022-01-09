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

from locale import getdefaultlocale
from typing import Optional
from vxt.misc.track_fmt import TrackFmt
from vxt.speech2text.engine import Speech2TextEngine
from vxt.speech2text.bing import BingSpeech2TextEngine
from vxt.speech2text.google import GoogleSpeech2TextEngine
from vxt.speech2text.google_cloud import GoogleCloudSpeech2TextEngine
from vxt.speech2text.houndify import HoundifySpeech2TextEngine
from vxt.speech2text.ibm import IbmSpeech2TextEngine
from vxt.speech2text.sphinx import SphinxSpeech2TextEngine


class Config(object):
    """App configuration"""

    def __init__(self) -> None:
        super().__init__()
        self.__engine: Speech2TextEngine = GoogleSpeech2TextEngine(None)
        locale = getdefaultlocale()[0]
        if locale:
            self.__language: str = locale
        else:
            self.__language: str = "en_US"
        self.__min_silence_len: int = 500
        self.__silence_threshold: int = -16
        self.__keep_silence: int = 500
        self.__output_fmt: TrackFmt = TrackFmt("%t-%s.64")
        self.__output_dir: Optional[str] = None

    @property
    def engine(self) -> Speech2TextEngine:
        return self.__engine

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str) -> None:
        self.__language = language

    @property
    def min_silence_len(self) -> int:
        return self.__min_silence_len

    @min_silence_len.setter
    def min_silence_len(self, len: int) -> None:
        self.__min_silence_len = len

    @property
    def silence_threshold(self) -> int:
        return self.__silence_threshold

    @silence_threshold.setter
    def silence_threshold(self, t: int) -> None:
        if t > 0:
            raise InvalidConfigError("Silence threshold should be a negative number")
        self.__silence_threshold = t

    @property
    def keep_silence(self) -> int:
        return self.__keep_silence

    @keep_silence.setter
    def keep_silence(self, how_much: int) -> None:
        if how_much < 0:
            raise InvalidConfigError(
                "Keep silence should be a positive integer bigger than or equal to 0"
            )
        self.__keep_silence = how_much

    @property
    def output_fmt(self) -> TrackFmt:
        return self.__output_fmt

    @output_fmt.setter
    def output_fmt(self, fmt: str) -> None:
        try:
            self.__output_fmt = TrackFmt(fmt)
        except Exception:
            raise InvalidConfigError("Invalid fmt syntax")

    @property
    def output_dir(self) -> str:
        return self.__output_dir

    @output_dir.setter
    def output_dir(self, d: str) -> None:
        self.__output_dir = d

    # -- speech 2 text setters

    def use_bing_speech2text(self, api_key: str) -> None:
        self.__engine = BingSpeech2TextEngine(api_key)

    def use_google_speech2text(self, api_key: Optional[str]) -> None:
        self.__engine = GoogleSpeech2TextEngine(api_key)

    def use_google_cloud_speech2text(self, credentials: Optional[str]) -> None:
        self.__engine = GoogleCloudSpeech2TextEngine(credentials)

    def use_houndify_speech2text(self, client_id: str, client_key: str) -> None:
        self.__engine = HoundifySpeech2TextEngine(client_id, client_key)

    def use_ibm_speech2text(self, username: str, password: str) -> None:
        self.__engine = IbmSpeech2TextEngine(username, password)

    def use_sphinx_speech2text(
        self, keyword_entries: Optional[str], grammar_file: Optional[str]
    ) -> None:
        self.__engine = SphinxSpeech2TextEngine(keyword_entries, grammar_file)


class InvalidConfigError(Exception):
    """
    Indicates an invalid configuration
    """

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return repr(self.message)

    def __repr__(self):
        return str(self.message)
