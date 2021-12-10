from solutions.common.parse import parse_input_as_list

OPENING_CHUNKS = ["(", "[", "{", "<"]
CLOSING_CHUNKS = [")", "]", "}", ">"]


def syntax_error_score(puzzle_input):
    syntax_errors = []

    for syntax_line in parse_input_as_list(puzzle_input):
        syntax_error = _find_syntax_error(syntax_line)
        if syntax_error:
            syntax_errors.append(syntax_error)
    print("Syntax error sum: {0}".format(
        _compute_syntax_error_score(syntax_errors)))


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


def _is_chunk_finished(opening_chunk, closing_chunk):
    return (OPENING_CHUNKS.index(opening_chunk)
            == CLOSING_CHUNKS.index(closing_chunk))


def _compute_syntax_error_score(syntax_errors):
    error_scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    error_sum = 0
    for syntax_error in syntax_errors:
        error_sum += error_scores[syntax_error]
    return error_sum
