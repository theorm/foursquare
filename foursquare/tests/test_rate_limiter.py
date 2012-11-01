#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging; log = logging.getLogger(__name__)

from . import BaseAuthenticatedEnpdointTestCase

class RateLimiterTestCase(BaseAuthenticatedEnpdointTestCase):
    """
    General
    """
    def test_rate_limiter_changing_hits(self):
        response = self.api.photos(self.default_photoid)
        assert 'photo' in response
        total1, remaining1 = self.api.base_requester.rate_limiter.rate_limit

        response = self.api.photos(self.default_photoid)
        assert 'photo' in response
        total2, remaining2 = self.api.base_requester.rate_limiter.rate_limit

        self.assertEqual(total1, total2)
        self.assertNotEqual(remaining1, remaining2)

    def test_rate_limiter_callback(self):
        captured_changes = []
        def capture_changes(hps):
            captured_changes.append(hps)

        self.api.base_requester.rate_limiter.set_callback(1, capture_changes)

        response = self.api.photos(self.default_photoid)
        assert 'photo' in response
        total1, remaining1 = self.api.base_requester.rate_limiter.rate_limit

        self.assertEqual(1, len(captured_changes))
