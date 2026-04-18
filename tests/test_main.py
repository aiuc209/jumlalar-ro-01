import pytest

def qisqartirish(jumlalar):
    yangi_jumlalar = []
    for jumla in jumlalar:
        sozlar = jumla.split()
        if len(sozlar) > 10:
            yangi_jumla = ' '.join(sozlar[:5])
        else:
            yangi_jumla = jumla
        yangi_jumlalar.append(yangi_jumla)
    return yangi_jumlalar

def test_qisqartirish():
    jumlalar = [
        "Bu birinchi jumla",
        "Bu jumla juda uzun va 10 dan ortiq sozdan iborat",
        "Bu jumla qisqa",
        "Bu jumla ham juda uzun va 10 dan ortiq sozdan iborat",
        "Bu jumla ham qisqa"
    ]
    expected_result = [
        "Bu birinchi jumla",
        "Bu jumla juda uzun va 10",
        "Bu jumla qisqa",
        "Bu jumla ham juda uzun va 10",
        "Bu jumla ham qisqa"
    ]
    assert qisqartirish(jumlalar) == expected_result

def test_qisqartirish_bo_sh():
    jumlalar = []
    expected_result = []
    assert qisqartirish(jumlalar) == expected_result

def test_qisqartirish_bitta_jumla():
    jumlalar = ["Bu birinchi jumla"]
    expected_result = ["Bu birinchi jumla"]
    assert qisqartirish(jumlalar) == expected_result

def test_qisqartirish_hammasi_uzun():
    jumlalar = [
        "Bu jumla juda uzun va 10 dan ortiq sozdan iborat",
        "Bu jumla ham juda uzun va 10 dan ortiq sozdan iborat",
        "Bu jumla juda juda uzun va 10 dan ortiq sozdan iborat"
    ]
    expected_result = [
        "Bu jumla juda uzun va 10",
        "Bu jumla ham juda uzun va 10",
        "Bu jumla juda juda uzun va 10"
    ]
    assert qisqartirish(jumlalar) == expected_result
