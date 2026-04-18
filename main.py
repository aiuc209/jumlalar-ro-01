def qisqartir(jumlalar):
    yangi_jumlalar = []
    for jumla in jumlalar:
        sozlar = jumla.split()
        if len(sozlar) > 10:
            yangi_jumla = ' '.join(sozlar[:5])
        else:
            yangi_jumla = jumla
        yangi_jumlalar.append(yangi_jumla)
    return yangi_jumlalar

jumlalar = ["Bu juda uzun jumla", "Qisqa jumla", "Bu jumla juda juda juda juda juda uzun"]
print(qisqartir(jumlalar))
