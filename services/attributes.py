class StagingArea:
    def __init__(self):
        self.stageds = []
        self.unstageds = []

    def add_stage_area(self, packed):
        if len(self.stageds) > 0:
            for sta in self.stageds:
                if sta == packed:
                    break
                else:
                    self.stageds.append(packed)
        else:
            self.stageds.append(packed)

    def add_unstage_area(self, packed):
        if len(self.unstageds) > 0:
            for sta in self.unstageds:
                if sta == packed:
                    break
                else:
                    self.unstageds.append(packed)
        else:
            self.unstageds.append(packed)

    def rm_unstage_area(self, packed):
        for sta in self.unstageds:
            if sta == packed:
                self.unstageds.remove(packed)