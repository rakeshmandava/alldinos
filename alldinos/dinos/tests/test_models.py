import pytest
from ..models import Dinosaur


# Connects our tests with our database
pytestmark = pytest.mark.django_db

def test___str__():
    dinosaur = Dinosaur.objects.create(name="t-rex",diet=CARNIVOROUS,)
    assert dinosaur.__str__() == "t-rex"
    assert str(dinosaur) == "t-rex"