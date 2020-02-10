"""Typing helpers."""

from typing import Any, Callable, Dict, Generator, Iterable, List, Mapping, Optional, Set, Tuple, Union
from pathlib import Path, PurePosixPath

from webob import Request, Response

from ..dispatch.core import Crumb
from .context import Context  # Make abstract?  :'(


# Types for WebCore extension component parts.

Tags = Set[str]  # Extension feature and dependency tags.
PositionalArgs = List[Any]  # Positional arguments to the endpoint callable.
KeywordArgs = Dict[str, Any]  # Keyword arguments to the endpoint callable.
Environment = Dict[str, Any]  # An interactive shell REPL environment.


# Types for WSGI component parts.

# Passed to the WSGI application.
WSGIEnvironment = Mapping[str, Any]

# Passed to start_response.
WSGIStatus = str
WSGIHeaders = Iterable[Tuple[str, str]]
WSGIException = Optional[Tuple[Any, Any, Any]]

# Returned by start_response.
WSGIWriter = Callable[[bytes], None]

WSGIResponse = Union[
		Generator[bytes, None, None],
		Iterable[bytes]
	]

# Types for core WSGI protocol components.

# Passed to the WSGI application.
WSGIStartResponse = Callable[[WSGIStatus, WSGIHeaders, WSGIException], WSGIWriter]

# WSGI application object itself.
WSGI = Callable[[WSGIEnvironment, WSGIStartResponse], WSGIResponse]


# Types relating to specific forms of callback utilized by the framework.

# The `serve` web application/server bridge API interface.
HostBind = str
PortBind = int
DomainBind = Optional[Union[str,Path]]
WebServer = Callable[..., None]  # [WSGI, HostBind, PortBind, ...]

# Serialization extension related typing.
SerializationTypes = Iterable[type]
Serializer = Callable[[Any], str]
Deserializer = Callable[[str], Any]
