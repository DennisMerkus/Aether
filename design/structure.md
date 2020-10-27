# World & Statement Structure

- Entities should be linkable through relations
- Events can be defined in different (fuzzy/vague) relative time periods (past, present, future)
- An agent's BDI modals can be used in creating statements and other utterances (want (in future), should (in future), should have (in past), etc)

Creating entities returns their id, which can then be used in defining relations between them.

## Statements

Statements include, implicitly or deduced from previous statements, extra information that qualifies certain ambiguous aspects of an utterance.
One clear example of this is deixis.
Another example is (assumed) shared background knowledge (about people, events/history, geographical knowledge).
Another example is things that a person has said earlier in the same conversation, or in a previous conversation.
Another example is events that the people involved in the conversation have witnessed together or are witnessing together.

## Usage of Ontological Primitives/Concepts

- Combine multiple concepts to describe an entity's category(s) and attributes
- Describe relationships between entities
- Describe state of entities
- Describe wanted state or past state
- Parse states to determine a statement's meaning, and vice versa, create a set of concepts to reflect an utterance
- Be general enough to provide easy annotation in existing game engines
- Words should be easily looked up through WordNet sense identifier, lemma, or a similar identifier; meaning a dictionary should be easily defined for translating between ontological concepts and grammatical patterns and vocabulary.

This means the concept definitions have to be:

- Composable: An entity might have multiple categories and relations that have to work together
- Link to other entities in the World/Utterance: A relation might refer to two entities that have been defined before. They should be linked to those entities. It's not allowed to specify relations on an entity that hasn't been defined.
- Data-driven: Annotations in game engines should be possible using some kind of format like JSON, using strings and simple objects that together, without the actual game engine's entities, represent the Mental World of a character.
- An extendable Lexicon for each language that handles vocabulary, grammar, named entities, and other essential linguistic information for all concepts
- A checker that determines whether a language has definitions for each concept defined in the ontology and warns for missing ones; including WordNet senses, and small dictionaries such as those for constructed languages.

## Matching Equivalence Rules


