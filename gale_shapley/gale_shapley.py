"""Gale-Shapley stable matching (proposer-optimal)."""
from __future__ import annotations

from collections import deque
from typing import Dict, Hashable, Sequence


def stable_matching(
    proposer_preferences: Dict[Hashable, Sequence[Hashable]],
    receiver_preferences: Dict[Hashable, Sequence[Hashable]],
) -> Dict[Hashable, Hashable]:
    """Return a proposer-optimal stable matching ``{proposer: receiver}``.

    Raises ``ValueError`` if the preference lists are inconsistent.
    """
    proposers = set(proposer_preferences)
    receivers = set(receiver_preferences)
    if len(proposers) != len(receivers):
        raise ValueError("proposer and receiver sets must have the same size")
    for p, prefs in proposer_preferences.items():
        if set(prefs) != receivers:
            raise ValueError(
                f"proposer {p!r} preferences must rank every receiver exactly once"
            )
    for r, prefs in receiver_preferences.items():
        if set(prefs) != proposers:
            raise ValueError(
                f"receiver {r!r} preferences must rank every proposer exactly once"
            )

    receiver_rank: Dict[Hashable, Dict[Hashable, int]] = {
        r: {p: i for i, p in enumerate(prefs)}
        for r, prefs in receiver_preferences.items()
    }
    next_proposal: Dict[Hashable, int] = {p: 0 for p in proposers}
    engagement: Dict[Hashable, Hashable] = {}        # receiver -> proposer
    free = deque(proposer_preferences)
    while free:
        proposer = free.popleft()
        choice = proposer_preferences[proposer][next_proposal[proposer]]
        next_proposal[proposer] += 1
        if choice not in engagement:
            engagement[choice] = proposer
        else:
            incumbent = engagement[choice]
            if receiver_rank[choice][proposer] < receiver_rank[choice][incumbent]:
                engagement[choice] = proposer
                free.append(incumbent)
            else:
                free.append(proposer)
    return {proposer: receiver for receiver, proposer in engagement.items()}


def is_stable(
    matching: Dict[Hashable, Hashable],
    proposer_preferences: Dict[Hashable, Sequence[Hashable]],
    receiver_preferences: Dict[Hashable, Sequence[Hashable]],
) -> bool:
    """Return ``True`` if ``matching`` has no blocking pair."""
    proposer_rank = {
        p: {r: i for i, r in enumerate(prefs)}
        for p, prefs in proposer_preferences.items()
    }
    receiver_rank = {
        r: {p: i for i, p in enumerate(prefs)}
        for r, prefs in receiver_preferences.items()
    }
    reverse = {receiver: proposer for proposer, receiver in matching.items()}
    for proposer, partner in matching.items():
        for other in proposer_preferences[proposer]:
            if other == partner:
                break
            if proposer_rank[proposer][other] >= proposer_rank[proposer][partner]:
                continue
            current_partner = reverse[other]
            if receiver_rank[other][proposer] < receiver_rank[other][current_partner]:
                return False
    return True
