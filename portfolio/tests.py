from django.test import Client, TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):
    fixtures = ["portfolio/test_galleries.json", "portfolio/test_posts.json"]

    def setUp(self):
        self.location = reverse("portfolio:home")
        self.client = Client()

    def test_get_allowed(self):
        """Fails if the response to a GET request is anything other than 200."""
        response = self.client.get(self.location)
        self.assertEqual(response.status_code, 200)

    def test_cache_control_header(self):
        """Fails if ``Cache-Control`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Cache-Control", response.headers.keys())

    def test_vary_hx_request_header(self):
        """Fails if ``Vary`` with value ``HX-Request`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Vary", response.headers.keys())
        self.assertIn("HX-Request", response.headers["Vary"])

    def test_full_template_used_on_non_htmx_request(self):
        """Fails if the full template wasn't rendered on non-htmx request."""
        expected_template_name = "portfolio/home.html"
        headers = {"HX-Request": "true", "HX-Boosted": "true"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)
        headers = {}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_main_partial_template_used_on_htmx_request(self):
        """Fails if the main partial template wasn't rendered on htmx request."""
        expected_template_name = "main"
        headers = {"HX-Request": "true", "HX-Boosted": "false"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_gallery_list_in_context(self):
        """Fails if ``gallery_list`` wasn't present in the response context."""
        response = self.client.get(self.location)
        self.assertIn("gallery_list", response.context)


class AboutViewTestCase(TestCase):
    def setUp(self):
        self.location = reverse("portfolio:about")
        self.client = Client()

    def test_get_allowed(self):
        """Fails if the response to a GET request is anything other than 200."""
        response = self.client.get(self.location)
        self.assertEqual(response.status_code, 200)

    def test_cache_control_header(self):
        """Fails if ``Cache-Control`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Cache-Control", response.headers.keys())

    def test_vary_hx_request_header(self):
        """Fails if ``Vary`` with value ``HX-Request`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Vary", response.headers.keys())
        self.assertIn(response.headers["Vary"], "HX-Request")

    def test_full_template_used_on_non_htmx_request(self):
        """Fails if the full template wasn't rendered on non-htmx request."""
        expected_template_name = "portfolio/about.html"
        headers = {"HX-Request": "true", "HX-Boosted": "true"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)
        headers = {}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_main_partial_template_used_on_htmx_request(self):
        """Fails if the main partial template wasn't rendered on htmx request."""
        expected_template_name = "main"
        headers = {"HX-Request": "true", "HX-Boosted": "false"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)


class ContactViewTestCase(TestCase):
    def setUp(self):
        self.location = reverse("portfolio:contact")
        self.client = Client()

    def test_get_allowed(self):
        """Fails if the response to a GET request is anything other than 200."""
        response = self.client.get(self.location)
        self.assertEqual(response.status_code, 200)

    def test_cache_control_header(self):
        """Fails if ``Cache-Control`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Cache-Control", response.headers.keys())

    def test_vary_hx_request_header(self):
        """Fails if ``Vary`` with value ``HX-Request`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Vary", response.headers.keys())
        self.assertIn("HX-Request", response.headers["Vary"])

    def test_full_template_used_on_non_htmx_request(self):
        """Fails if the full template wasn't rendered on non-htmx request."""
        expected_template_name = "portfolio/contact.html"
        headers = {"HX-Request": "true", "HX-Boosted": "true"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)
        headers = {}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_main_partial_template_used_on_htmx_request(self):
        """Fails if the main partial template wasn't rendered on htmx request."""
        expected_template_name = "main"
        headers = {"HX-Request": "true", "HX-Boosted": "false"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_form_in_context(self):
        """Fails if ``form`` wasn't in the response context."""
        response = self.client.get(self.location)
        self.assertIn("form", response.context)


class ContactFormViewTestCase(TestCase):
    def setUp(self):
        self.location = reverse("portfolio:contact form")
        self.client = Client()

    def test_get_allowed(self):
        """Fails if the response to a GET request is anything other than 200."""
        response = self.client.get(self.location)
        self.assertEqual(response.status_code, 200)

    def test_post_allowed(self):
        """Fails if the response to a POST request is anything other than 200."""
        response = self.client.post(self.location)
        self.assertEqual(response.status_code, 200)

    def test_cache_control_header(self):
        """Fails if ``Cache-Control`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Cache-Control", response.headers.keys())

    def test_vary_hx_request_header(self):
        """Fails if ``Vary`` with value ``HX-Request`` wasn't in the response headers."""
        response = self.client.get(self.location)
        self.assertIn("Vary", response.headers.keys())
        self.assertIn("HX-Request", response.headers["Vary"])

    def test_full_template_used_on_non_htmx_request(self):
        """Fails if the full template wasn't rendered on non-htmx request."""
        expected_template_name = "portfolio/contact_form.html"
        headers = {"HX-Request": "true", "HX-Boosted": "true"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)
        headers = {}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)

    def test_main_partial_template_used_on_htmx_request(self):
        """Fails if the main partial template wasn't rendered on htmx request."""
        expected_template_name = "main"
        headers = {"HX-Request": "true", "HX-Boosted": "false"}
        response = self.client.get(self.location, headers=headers)
        self.assertTemplateUsed(response, expected_template_name)
