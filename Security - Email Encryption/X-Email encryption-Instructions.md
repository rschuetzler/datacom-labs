---
header-includes:
- \usepackage{xcolor}
- \definecolor{Light}{gray}{0.90}
- \let\OldTexttt\texttt
- \renewcommand{\texttt}[1]{\OldTexttt{\colorbox{Light}{#1}}}
---
Email Encryption Lab
==========================

For this lab, you will use public key encryption to send and receive encrypted
emails. You will receive full credit after you send me your public key, receive
and decrypt my reply, and respond. To give me time to respond, your first
message to me must be sent by 8am on the day the assignment is due.  I will
reply, and you must respond to my reply by the due date and time.

# Installing and configuring GPG and Thunderbird

1.  Go to <https://www.mozilla.org/en-US/thunderbird/download> to download and install the Mozilla
    Thunderbird email client
2.  Set up Thunderbird to use whatever email address you want to use for this lab. The
    easiest is probably a Gmail address rather than your email.arizona.edu address.
    1.  If you want to use Gmail, make sure that you have IMAP enabled. Do this by
        clicking the gear icon and selecting "Settings." Then go to the "Forwarding and
        POP/IMAP tab" and select "Enable IMAP."
    2.  If you're still having trouble getting it set up, there is a link to
        configuration instructions at the bottom of that page.  Follow
        [these instructions](https://support.google.com/mail/troubleshooter/1668960?rd=1#ts=1665018,1665141)
        to configure Gmail in Thunderbird.
3.  On Windows, go to <http://www.gpg4win.org/> to download GPG (the Gnu Privacy Guard).
    1.  On a Mac, go to <http://gpgtools.org/> to download GPG Tools. After you install, it
        will ask if you wish to run GPGtools. Just close it, as we will generate our keys
        through Thunderbird.
4.  Install the GPG implementation for whichever platform you are using (Windows
or Mac)
    * For GPG4win, make sure you check the box to also install Kleopatra during
      the installation
5.  Once you have both GPG and Thunderbird installed, install the Enigmail add-on for
    Thunderbird (<https://addons.mozilla.org/en-us/thunderbird/addon/enigmail/>).
6.  Restart Thunderbird, and you will be prompted to configure Enigmail
7.  Follow the setup wizard prompts to generate your public and private keys
    1.  Select "Convenient auto encryption" when it is displayed. Also select to sign all
        of your messages by default.
    2.  Opt to "Create a new key pair" and follow the instructions on screen.
    3.  When prompted, you may create the revocation certificate if you wish. You won't
        need it for this lab, but if you want to continue using email encryption, it's a
        good idea.

# Exchanging public keys and sending emails

As discussed in class, asymmetric (public key) encryption works because you can share
your public key with anyone, and they can use that public key to encrypt a message
meant just for you. In this section of the lab we will exchange public keys so that
we can send each other encrypted messages

1.  Press the "Alt" key to bring up the menu in Thunderbird.
2.  Select "Enigmail" and then "Key Management"
3.  You will be presented with a list of keys installed on your computer (probably just
    your own)
4.  Install my public key
    1.  Download the appropriate public key file (Ryan.asc) from Blackboard.
    2.  In the "Key Management" window, select "File" -> "Import keys from file"
    3.  Right-click on the new key and select "Sign key". Signing keys is your way of
        indicating that you trust they key, and that you believe it truly belongs to me.
5.  Send me your own public key
    1.  Now that you have my public key, you can send me an encrypted message. Send me
        your own public key in an encrypted message using the following steps:
    2.  Right-click your own name in the "Key Management" window and select "Send Public
        Keys by Email"
    3.  Enter my gmail address (rschuet@gmail.com) as the destination and "ISQA
        3400 Encryption lab" in the subject line. 
    4.  In the body of the email. Tell me something interesting. Could be a fact, a
        story, what you did last summer, or what you are doing this summer. It doesn't
        matter, just say something that I can respond to.
    5.  Select the option to "Encrypt and sign the message text, but not the
        attachments." This will send your public key in plain text.  Remember that
        that's okay; anybody can have your public key and it won't compromise your own
        security.  So there's no harm in having your public key intercepted or shared.
6.  Respond to my message
    1.  To verify that you are able to both encrypt and decrypt a message, I will send
        you a response to your message from step 5. To complete the lab, you need to
        reply to my message. Make sure you keep my response in the body of your reply so
        I can verify that you received and decrypted it.

# If you'd rather

It is possible to send encrypted mail with Apple Mail, or through your webmail
client like Gmail, Yahoo, etc.
([webmail instructions](http://lifehacker.com/how-to-encrypt-your-email-and-keep-your-conversations-p-1133495744)).
If you would rather do that, you may. The only true requirement for this lab is
that you send me an encrypted message and respond to my encrypted reply. I don't
care how you do it, but I've only provided instructions for how to do it in
Thunderbird. Feel free to use Google to find out how to send GPG encrypted
messages if you have a different preferred email client.
