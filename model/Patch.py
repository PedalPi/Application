# -*- coding: utf-8 -*-
from model.Effect import Effect


class Patch(object):
    json = None
    bank = None

    def __init__(self, json, bank=None):
        self.bank = bank
        self.json = json

    def __getitem__(self, key):
        return self.json[key]

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
           and self.json == other.json

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def effects(self):
        returned = []
        effects = self.json["effects"]

        for effectJson in effects:
            returned.append(Effect(effectJson, self))

        return returned

    def addEffect(self, effect):
        self["effects"].append(effect.json)
        effect.patch = self

    def indexOfEffect(self, effect):
        return self["effects"].index(effect.json)