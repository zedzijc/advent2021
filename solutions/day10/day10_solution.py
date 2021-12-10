from solutions.common.parse import parse_input_as_list
import math

OPENING_CHUNKS = ["(", "[", "{", "<"]
CLOSING_CHUNKS = [")", "]", "}", ">"]


def complete_syntax_score(puzzle_input):
    completion_scores = []
    for syntax_line in parse_input_as_list(puzzle_input):
        completion_score = _find_syntax_score(syntax_line)
        if completion_score:
            completion_scores.append(completion_score)
    completion_scores.sort()
    print("Total syntax sum: {0}".format(
        completion_scores[math.floor(len(completion_scores) / 2)]))


def syntax_error_score(puzzle_input):
    syntax_errors = []

    for syntax_line in parse_input_as_list(puzzle_input):
        syntax_error = _find_syntax_error(syntax_line)
        if syntax_error:
            syntax_errors.append(syntax_error)
    print("Syntax error sum: {0}".format(
        _compute_error_score(syntax_errors)))


def _find_syntax_error(syntax_line):
    open_chunks = []
    syntax_error = ""
    for part in syntax_line:
        if part in OPENING_CHUNKS:
            open_chunks.append(part)
        elif part in CLOSING_CHUNKS:
            if not open_chunks:  # Closing chunk without having any open chunks
                syntax_error = part
                break
            elif _is_chunk_finished(open_chunks[-1], part):
                del open_chunks[-1]
            else:  # Unmatched closing chunk
                syntax_error = part
                break
        else:
            print("Received an illegal chunk part: {0}".format(part))
            break
    return syntax_error


def _find_syntax_score(syntax_line):
    open_chunks = []
    completed_chunks = []
    for part in syntax_line:
        if part in OPENING_CHUNKS:
            open_chunks.append(part)
        elif part in CLOSING_CHUNKS:
            if not open_chunks:  # Closing chunk without having any open chunks
                completed_chunks.clear()
                open_chunks.clear()
                break
            elif _is_chunk_finished(open_chunks[-1], part):
                del open_chunks[-1]
            else:  # Unmatched closing chunk
                completed_chunks.clear()
                open_chunks.clear()
                break
        else:
            print("Received an illegal chunk part: {0}".format(part))
            break
    for open_chunk in reversed(open_chunks):
        completed_chunks += _get_closing_chunk(open_chunk)
    return _compute_completion_score(completed_chunks)


def _get_closing_chunk(opening_chunk):
    if opening_chunk in OPENING_CHUNKS:
        return CLOSING_CHUNKS[OPENING_CHUNKS.index(opening_chunk)]


def _is_chunk_finished(opening_chunk, closing_chunk):
    return (OPENING_CHUNKS.index(opening_chunk)
            == CLOSING_CHUNKS.index(closing_chunk))


def _compute_error_score(entries):
    error_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    score = 0
    for entry in entries:
        score += error_scores[entry]
    return score


def _compute_completion_score(entries):
    completion_scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    score = 0
    for entry in entries:
        score *= 5
        score += completion_scores[entry]
    return score
