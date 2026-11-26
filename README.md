# The Painfully Honest Out-of-Office

[![competition](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/vickyair1/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/vickyair1/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

One out-of-office email auto-reply, at most 200 characters, painfully honest
about the sender's absence, inbox and enthusiasm, yet still polite enough a
manager would let it stand.

Entry for [The Painfully Honest Out-of-Office](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
on [make.fun](https://make.fun).

## The line

> I'm away until Monday, resting the enthusiasm my inbox has spent; I'll answer the urgent ones first and the rest once I've forgiven them.

137 characters. It admits the private truth (the inbox has spent the sender's
enthusiasm, and not every email gets answered — the urgent ones first, the
rest only once forgiven) in a warm tone, and the turn — forgiving the emails,
as if the inbox wronged the sender — is the image a reader quotes to a
colleague.

## Run

```sh
python3 main.py
```

Prints the single line to stdout and writes it to `/output/entry.txt`
(override with `MAKEFUN_OUTPUT_DIR`). The program refuses to write a line
that is empty, multi-line, or over 200 characters.

## License

MIT — see [LICENSE](LICENSE).
