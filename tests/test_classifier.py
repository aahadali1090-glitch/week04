from ai_service.services.rule_classifier import RuleClassifier


def test_password_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I forgot my password")

    assert result == "account"


def test_fee_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I have a fee problem")

    assert result == "finance"


def test_technical_classification():
    classifier = RuleClassifier()

    result = classifier.classify("The server is down")

    assert result == "technical"


def test_unknown_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"