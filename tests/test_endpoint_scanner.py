"""Tests for the endpoint scanner module."""

from hades_endpoint.endpoint_scanner import EndpointScanner


def test_endpoint_scanner_initialization():
    """Test EndpointScanner initialization."""
    scanner = EndpointScanner()
    assert scanner is not None
    assert scanner.results == []


def test_run_scan():
    """Test run_scan method."""
    scanner = EndpointScanner()
    results = scanner.run_scan()
    
    assert len(results) == 3
    assert results[0]["check"] == "open_ports"
    assert results[1]["check"] == "services"
    assert results[2]["check"] == "configurations"


def test_check_open_ports():
    """Test check_open_ports method."""
    scanner = EndpointScanner()
    scanner.check_open_ports()
    
    assert len(scanner.results) == 1
    assert scanner.results[0]["check"] == "open_ports"
    assert scanner.results[0]["status"] == "pass"


def test_check_services():
    """Test check_services method."""
    scanner = EndpointScanner()
    scanner.check_services()
    
    assert len(scanner.results) == 1
    assert scanner.results[0]["check"] == "services"
    assert scanner.results[0]["status"] == "pass"


def test_check_configurations():
    """Test check_configurations method."""
    scanner = EndpointScanner()
    scanner.check_configurations()
    
    assert len(scanner.results) == 1
    assert scanner.results[0]["check"] == "configurations"
    assert scanner.results[0]["status"] == "pass"
