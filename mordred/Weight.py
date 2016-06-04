from rdkit.Chem.Descriptors import ExactMolWt

from ._base import Descriptor


__all__ = (
    'Weight',
)


class Weight(Descriptor):
    r"""molecular weight descriptor.

    :type averaged: bool
    :param averaged: averaged by number of atom
    """

    explicit_hydrogens = True

    @classmethod
    def preset(cls):
        yield cls(False)
        yield cls(True)

    def __str__(self):
        return 'AMW' if self._averaged else 'MW'

    __slots__ = ('_averaged',)

    def as_key(self):
        return self.__class__, (self._averaged,)

    def __init__(self, averaged=False):
        self._averaged = averaged

    def calculate(self):
        w = ExactMolWt(self.mol)
        if self._averaged:
            w /= self.mol.GetNumAtoms()

        return w

    rtype = float
