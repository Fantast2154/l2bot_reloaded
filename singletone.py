from __future__ import annotations


class Singletone:
    instance = None

    @classmethod
    def get_instance(cls) -> Singletone:
        if cls.instance is None:
            cls.instance = Singletone()
        return cls.instance


if __name__ == '__main__':
    a = Singletone.get_instance()
    print(a)

    b = Singletone.get_instance()
    print(b)
