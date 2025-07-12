cidade = " ".join(
    str(input("Em qual cidade você nasceu? ")).strip().title().split()
)
print(f"Sua cidade {"" if "Santos" in cidade else "não "}tem Santos no nome!")