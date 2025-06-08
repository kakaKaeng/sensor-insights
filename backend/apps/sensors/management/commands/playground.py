from typing import Any

from django.core.management import BaseCommand


SWAP_LETTERS = {
    '(': ')',
    ')': '(',
    '<': '>',
    '>': '<',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '[',
    '|': '|',
}

class Command(BaseCommand):
    help = 'Playground command for DEBUG and Testing'

    @staticmethod
    def swap_letter(x) -> str:
        return SWAP_LETTERS[x]

    def is_valid(self, txt: str) -> bool:
        if txt.count('|') % 2 != 0:
            return False

        return all(
            map(
                lambda x: ''.join(list(map(self.swap_letter, x))) == x[::-1], txt.split('||')
            )
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """

        {<>}|(<{}>)|<<

        0 {<>} => }><{ === }><{ = true
        1 }><{ = true
        2 << => >> === << = false

        """
        input1 = '{<>}||(<{}>)|<<'
        input2 = '{<>}||(<{}>)||<{}>'
        input3 = '|<[>||'
        input4 = '|<[((())))]>|'
        input5 = '{}[]'


        # print(input1, self.is_valid(input1))
        # print(input2, self.is_valid(input2))
        # print(input3, self.is_valid(input3))
        # print(input4, self.is_valid(input4))
        print(input5, self.is_valid(input5))
