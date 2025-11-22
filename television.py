class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:

        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL
        self._saved_volume: int = self._volume

    def power(self) -> None:
        """
        Toggles power status
        """
        self._status = not self._status

    def mute(self) -> None:
        """
        toggles mute when tv powered on and saves volume
        """
        if self._status:
            if self._status:
                self._muted = not self._muted
                if self._muted:
                    self._saved_volume = self._volume
                    self._volume = 0
                else:
                    self._volume = self._saved_volume

    def channel_up(self) -> None:
        """
        increases tv channel, cycling to min if at max
        """
        if self._status:
            if self._channel == Television.MAX_CHANNEL:
                self._channel = Television.MIN_CHANNEL
            else:
                self._channel += 1

    def channel_down(self) -> None:
        """
        increase tv channel, cycling to max if at min

        """
        if self._status:
            if self._channel == Television.MIN_CHANNEL:
                self._channel = Television.MAX_CHANNEL
            else:
                self._channel -= 1

    def volume_up(self) -> None:
        """
        increases tv volume
        if muted, unmute first
        """
        if self._status:
            if self._muted:
                self.mute()
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """
        decreases tv volume
        if muted, unmute first
        """
        if self._status:
            if self._muted:
                self.mute()
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        returns a string representation of the television status
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

