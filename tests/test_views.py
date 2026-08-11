import tempfile
import pytest

from django.test import Client
from django.urls import reverse
from portfolio.models import Gallery, Post


@pytest.fixture
def client():
    yield Client()


@pytest.fixture(autouse=True)
def gallery():
    yield Gallery.objects.create(pk=1, name="Gallery 1", slug="gallery-1")


@pytest.fixture(autouse=True)
def post(gallery):
    yield Post.objects.create(
        gallery=gallery, file=tempfile.NamedTemporaryFile(suffix=".jpg").name
    )


@pytest.mark.parametrize(
    "path",
    [
        reverse("portfolio:home"),
        reverse("portfolio:about"),
        reverse("portfolio:contact"),
        reverse("portfolio:gallery list"),
        reverse(
            "portfolio:gallery detail",
            kwargs={"gallery_pk": 1, "gallery_slug": "gallery-1"},
        ),
        reverse(
            "portfolio:post detail",
            kwargs={
                "gallery_pk": 1,
                "gallery_slug": "gallery-1",
                "post_pk": 1,
            },
        ),
    ],
)
@pytest.mark.django_db
def test_get_allowed(client, path):
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "path",
    [
        reverse("portfolio:home"),
        reverse("portfolio:about"),
        reverse("portfolio:contact"),
        reverse("portfolio:gallery list"),
        reverse(
            "portfolio:gallery detail",
            kwargs={"gallery_pk": 1, "gallery_slug": "gallery-1"},
        ),
        reverse(
            "portfolio:post detail",
            kwargs={
                "gallery_pk": 1,
                "gallery_slug": "gallery-1",
                "post_pk": 1,
            },
        ),
    ],
)
@pytest.mark.django_db
def test_cache_control_header(client, path):
    response = client.get(path)
    assert response.has_header("Cache-Control")


@pytest.mark.parametrize(
    "path",
    [
        reverse("portfolio:home"),
        reverse("portfolio:about"),
        reverse("portfolio:contact"),
        reverse("portfolio:gallery list"),
        reverse(
            "portfolio:gallery detail",
            kwargs={"gallery_pk": 1, "gallery_slug": "gallery-1"},
        ),
        reverse(
            "portfolio:post detail",
            kwargs={
                "gallery_pk": 1,
                "gallery_slug": "gallery-1",
                "post_pk": 1,
            },
        ),
    ],
)
@pytest.mark.django_db
def test_vary_on_hx_request_header(client, path):
    response = client.get(path)
    assert response.has_header("Vary")
    assert "HX-Request" in response.headers["Vary"]
