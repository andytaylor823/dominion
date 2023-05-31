def CardSelector(state, decisionResponse, scoring_function):
    cardChoices = state.decision.cardChoices.copy() # defensive copy
    cardChoices = sorted(cardChoices, key=lambda c: scoring_function(c), reverse=True) # descending

    for i in range(max(1, state.decision.minimumCards)):
        decisionResponse.cards.append(cardChoices[i])