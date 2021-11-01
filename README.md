# StegAma
## StegAma is a simple python GUI steganography tool

### About
Steganography is a technique that allows you to conceal a message inside another message or object.
For example you could hide a text inside an image and, by doing so, the very existence of the
concealed text is kept secret.

Steganography differ from cryptography because in cryptography, the encrypted message is in
plain sight (but it is unreadable without the key) while in steganography the message is hidden
inside another object so no one know that a communication even occurred.

### Instructions
After launching the script.

#### To hide text into an image
1. Write your secret text in the text field
2. Click the "Encode" button
3. Choose an image
4. The tool then creates a new image named "secret_image.png" with the secret text hidden inside

#### To reveal hidden text
1. Click the "Decode" button
2. The tool prompts you to choose the image with the hidden text
3. You can find the revealed text in the text field

### Specifications
StegAma make use of the **stegano** python package to implement the LSB steganography technique with
the use of sets.
Allowed input image type (so far) are: .JPG, .JPEG, .PNG

The GUI is built with the Tkinter package.
