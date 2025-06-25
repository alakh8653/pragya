"""WASM kernel placeholder."""


def execute(bytecode: bytes) -> bytes:
    """Pretend to execute WebAssembly code."""
    return bytecode[::-1]
