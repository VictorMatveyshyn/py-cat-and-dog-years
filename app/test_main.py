import pytest

from app.main import get_human_age, AgeError


class TestConvertCatDogAges:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0,
                14,
                [0, 0],
                id="should get human age before 15 catdog ages"
            ),
            pytest.param(
                15,
                23,
                [1, 1],
                id="should get human age between 15-24 catdog ages"
            ),
            # test_should_get_human_age_more_then_24_catdog_ages
            pytest.param(
                100,
                100,
                [21, 17],
                id="should get human age more then 24 catdog ages"
            )
        ]
    )
    def test_convert_cat_dog_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestWrongInput:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                -1,
                -2,
                ValueError,
                id="negative animal age input"
            ),
            # test_tolong_animal_age
            pytest.param(
                155,
                270,
                AgeError,
                id="tolong animal age"
            )

        ]
    )
    def test_raisim(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: BaseException
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
