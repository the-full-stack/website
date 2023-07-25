---
title: "RWKV, Explained"
description: "A step-by-step explanation of the RWKV architecture via typed PyTorch code."
author: "Charles Frye"
hide:
  - navigation
tags:
  - llms
  - rwkv
  - code
  - notebook
embed_image: https://i.imgur.com/W3mhy9f.png
time: "2023-07-25"
---
<div class="author" markdown>
By [Charles Frye](https://twitter.com/charles_irl).
</div>

--8<-- "blog/posts/rwkv-explainer/.content.md"

## Acknowledgements

Thanks to
[Ryan Zarcone](https://twitter.com/r_zarcone)
for several long {white,chalk}boarding sessions on RWKV
and to
[Igor Vasiljevic](https://twitter.com/vslevic),
[Faris Hijazi](https://twitter.com/theeFaris),
[Rogério Chaves](https://twitter.com/_rchaves_),
and
[Ben Field](https://twitter.com/benfieldddd)
for helpful comments on drafts.

Also, many thanks to the RWKV team,
in particular
[Johan Wind](https://johanwind.github.io),
whose
[blog post](https://johanwind.github.io/2023/03/23/rwkv_details.html)
implementing RWKV in numpy was an invaluable resource
and provided the initial scaffolding for the code in this post.
