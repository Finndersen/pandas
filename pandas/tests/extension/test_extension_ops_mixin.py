from pandas.core.arrays import ExtensionArray, ExtensionScalarOpsMixin
import pytest


class CustomOperator(Exception):
    """
    Exception raised by custom operator methods to verify it has not been overridden
    """
    pass


class EAWithCustomOps(ExtensionScalarOpsMixin, ExtensionArray):
    # Custom operator methods
    def __add__(self, other):
        raise CustomOperator

    def __gt__(self, other):
        raise CustomOperator

    def __and__(self, other):
        raise CustomOperator


EAWithCustomOps._add_arithmetic_ops()
EAWithCustomOps._add_comparison_ops()
EAWithCustomOps._add_logical_ops()


class TestExtensionScalarOpsMixin:
    def test_arithmetic_operators(self, all_arithmetic_operators):
        # Verify methods added
        op_name = all_arithmetic_operators
        assert hasattr(EAWithCustomOps, op_name)

    def test_operators_not_overridden(self):
        # Verify the custom operator methods were not overridden
        ea = EAWithCustomOps()
        with pytest.raises(CustomOperator):
            ea.__and__(10)

        with pytest.raises(CustomOperator):
            ea.__gt__(10)

        with pytest.raises(CustomOperator):
            ea.__and__(10)
