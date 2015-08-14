import pytest
from leafman.trie import Trie


class TestTrie:
    @pytest.fixture
    def trie(self):
        return Trie([
            'abc',
            'abcdef',
            'def',
            ])

    def test_trie_get(self, trie):
        assert trie.get('abc') == ['abc', 'abcdef']
        assert trie.get('def') == ['def']
        assert set(trie.get('')) == set(['abc', 'def', 'abcdef'])

    def test_trie_insert(self, trie):
        trie.insert('defg')
        assert trie.get('def') == ['def', 'defg']
