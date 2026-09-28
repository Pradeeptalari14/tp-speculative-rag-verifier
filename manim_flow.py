from manim import *

class SpeculativeRAGAnimation(Scene):
    def construct(self):
        title = Text("Speculative RAG & Self-Correction Pipeline", font_size=32, color=TEAL)
        title.to_edge(UP)
        self.play(Write(title))

        retriever = Rectangle(width=3, height=1.5, color=BLUE).shift(LEFT * 4)
        ret_txt = Text("Hybrid Retrieval\n(Vector + BM25)", font_size=16).move_to(retriever)

        draft = Rectangle(width=3, height=1.5, color=CYAN).shift(LEFT * 0)
        draft_txt = Text("Draft SLM (1.5B)\n(~140 tok/s)", font_size=16).move_to(draft)

        verifier = Rectangle(width=3, height=1.5, color=GREEN).shift(RIGHT * 4)
        ver_txt = Text("Verifier Judge (70B)\n(Single-Pass Check)", font_size=16).move_to(verifier)

        a1 = Arrow(retriever.get_right(), draft.get_left(), color=YELLOW)
        a2 = Arrow(draft.get_right(), verifier.get_left(), color=YELLOW)

        self.play(Create(retriever), Write(ret_txt))
        self.play(GrowArrow(a1), Create(draft), Write(draft_txt))
        self.play(GrowArrow(a2), Create(verifier), Write(ver_txt))
        self.wait(1)
