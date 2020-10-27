class PhysicalSpace(object):
    """
    Abstract representation of 3D space.
    """

    def contains(self, entity) -> bool:
        raise NotImplementedError()

    def in_front_of(self, A, B) -> bool:
        raise NotImplementedError()


class ThreeDimensionalSpace(PhysicalSpace):
    """
    An implementation of a 3D space such as we're used to.

    With actual dimensions, and measurements between objects;
    i.e. not a a conceptual representation.
    """

    pass
