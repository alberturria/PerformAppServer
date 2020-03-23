class WaveEntity(object):
    def __init__(self, id, muscle, rms, raw, avg_rms, mvc, historic_mvc):
        self._id = id
        self._muscle = muscle
        self._rms = rms
        self._raw = raw
        self._avg_rms = avg_rms
        self._mvc = mvc
        self._historic_mvc = historic_mvc
