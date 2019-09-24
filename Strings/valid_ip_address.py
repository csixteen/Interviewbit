#!/usr/bin/env python3
# coding: utf-8
import unittest


class Solution:
    def create_ips(self, S, i, octet):
        if octet == 4:
            return [S[i:i+j+1] for j in range(0, min(3, len(S) - (4 - octet) - i))]
        else:
            res = []
            for j in range(0, min(3, len(S) - (4 - octet) - i)):
                for r in self.create_ips(S, i+j+1, octet + 1):
                    res.append('{}.{}'.format(S[i:i+j+1], r))

            return res

    def restoreIPAddresses(self, A):
        def is_valid_ip(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False

            return all([
                (1 <= len(x) <= 3) and \
                        not (x.startswith('0') and len(x) > 1) and \
                        (0 <= int(x) <= 255) \
                        for x in parts
            ])

        ips = list(filter(lambda x: len(x) == len(A) + 3, self.create_ips(A, 0, 1)))

        return list(filter(lambda x: is_valid_ip(x), ips))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ("0100100", ["0.10.0.100", "0.100.10.0"]),
            ("0000000", []),
            ("25525511135", ["255.255.111.35", "255.255.11.135"])
        ]

    def test_restoreIPAddresses(self):
        s = Solution()
        for i, e in self.test_cases:
            self.assertEqual(sorted(s.restoreIPAddresses(i)), sorted(e))


if __name__ == '__main__':
    unittest.main(verbosity=2)

