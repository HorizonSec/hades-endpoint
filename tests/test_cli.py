"""Tests for the CLI module."""

import sys
from unittest.mock import patch
from hades_endpoint.cli import main


def test_main_no_args():
    """Test main function with no arguments."""
    with patch.object(sys, 'argv', ['hades']):
        result = main()
        assert result == 0


def test_main_unknown_command():
    """Test main function with unknown command."""
    with patch.object(sys, 'argv', ['hades', 'unknown']):
        result = main()
        assert result == 1


def test_main_scan_command():
    """Test main function with scan command."""
    with patch.object(sys, 'argv', ['hades', 'scan']):
        result = main()
        assert result == 0
