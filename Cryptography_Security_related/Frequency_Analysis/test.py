import unittest
from cipher import Cipher


class FreqAnalysisCracker(unittest.TestCase):

    def test_1(self):
        cipher = Cipher()
        cipher_text = "Khoor Zruog ! Frqjudwxodwlrqv, brx kdyh vxffhvvixoob ghfubswhg ph ! Kdyh ixq zlwk wklv sxccoh"
        expected_text = "Hello world ! congratulations, you have successfully decrypted me ! have fun with this puzzle"
        self.assertEqual(cipher.shift_find(cipher_text),expected_text)

    def test_2(self):
        cipher = Cipher()
        cipher_text = "Iye mkx pyyv kvv yp dro zoyzvo cywo yp dro dswo, kxn cywo yp dro zoyzvo kvv yp dro dswo, led iye mkx'd pyyv kvv yp dro zoyzvo kvv yp dro dswo."
        expected_text = "You can fool all of the people some of the time, and some of the people all of the time, but you can't fool all of the people all of the time."
        self.assertEqual(cipher.shift_find(cipher_text), expected_text)

    def test_3(self):
        cipher = Cipher()
        cipher_text = "Obm qcrs mci'js pssb kfwhwbu tcf 6 acbhvg cf acfs kwhvcih zccywbu oh wh awuvh og kszz vojs pssb kfwhhsb pm gcascbs szgs"
        self.assertEqual(cipher.shift_find(cipher_text),
                         "Any code you've been writing for 6 months or more without looking at it might as well have been written by someone else")

    def test_4(self):
        cipher = Cipher()
        cipher_text = "Kp. ylb Kpq. Bspqjcw, md lskzcp dmsp, Npgtcr Bpgtc, ucpc npmsb rm qyw rfyr rfcw ucpc ncpdcarjw lmpkyj, rfyli wms tcpw ksaf. Rfcw ucpc rfc jyqr ncmnjc wms’b cvncar rm zc gltmjtcb gl ylwrfgle qrpylec mp kwqrcpgmsq, zcaysqc rfcw hsqr bgbl’r fmjb ugrf qsaf lmlqclqc. Kp. Bspqjcw uyq rfc bgpcarmp md y dgpk ayjjcb Epsllgleq, ufgaf kybc bpgjjq. Fc uyq y zge, zccdw kyl ugrf fypbjw ylw lcai, yjrfmsef fc bgb fytc y tcpw jypec ksqryafc. Kpq. Bspqjcw uyq rfgl ylb zjmlbc ylb fyb lcypjw rugac rfc sqsyj ykmslr md lcai, ufgaf aykc gl tcpw sqcdsj yq qfc qnclr qm ksaf md fcp rgkc apylgle mtcp eypbcl dclacq, qnwgle ml rfc lcgefzmpq. Rfc Bspqjcwq fyb y qkyjj qml ayjjcb Bsbjcw ylb gl rfcgp mnglgml rfcpc uyq lm dglcp zmw ylwufcpc. Rfc Bspqjcwq fyb ctcpwrfgle rfcw uylrcb, zsr rfcw yjqm fyb y qcapcr, ylb rfcgp epcyrcqr dcyp uyq rfyr qmkczmbw umsjb bgqamtcp gr. Rfcw bgbl’r rfgli rfcw amsjb zcyp gr gd ylwmlc dmslb msr yzmsr rfc Nmrrcpq."
        self.assertEqual(cipher.shift_find(cipher_text), "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense. Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters.")

