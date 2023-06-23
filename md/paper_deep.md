# Exploring Deep Learning: How Neural Networks Can Be Used to Recognize Handwritten Digits

## Abstract

Deep learning offers us an alternative way to approach problem-solving that differs from traditional algorithmic methods. Instead of telling the algorithm what to do, one can just show it lots of examples. This can significantly reduce development time, as it eliminates the need for complex logical rules and patterns. Furthermore, it makes it easier to scale and customize the product because just modifying the training data enables a neural network to learn and adapt new behaviors efficiently.

Deep neural networks are biologically inspired computational systems composed of multiple layers that process some input data based on internal parameters. Those parameters are learned and adjusted over time using the *backpropagation* algorithm.

Furthermore, the use of statistical instead of logical methods to analyze and solve problems makes it possible to quickly solve tasks that would have required significant programming effort using conventional approaches like speech, object, or handwriting recognition, which is what I will focus on in this paper.

Our approach involves revisiting the theoretical background of deep learning and its major components in [part 1](#theory), followed by the application of these concepts to model and train a deep neural network capable of recognizing handwritten digits from scratch in [part 2](#praxis).

<a id="theory"></a>
## What is a neural network and how does it work? 

### Biological motivation
In order to develop an intuitive understanding of artificial neural networks, it is beneficial to briefly explore the biological background of neural networks and the learning processes that occur in the human brain. This exploration helps to establish a direct connection between the biological foundation and the understanding of artificial neural networks (ANN’s).

The human brain consists of approximately 86 billion neurons which are densely connected to thousands of other neurons. These connections, called synapses, get strengthened when signals are repeatedly transmitted between them. This long-lasting amplification of synaptic transmissions is called *long-term potentiation* (LTP), and is the cellular and molecular foundation of learning. Through continuous repetition of experiences and actions certain networking patterns are formed and new synapses are created or intensified while ones that were used less get dismantled over time. For example, if someone learns a new skill, such as playing the piano, certain synapses in their brain will become stronger and more efficient, allowing them to play the piano better over time. This ability to form new connections and adjust existing connections based on their importance is called *neuroplasticity*. [[Groß et al. 2021]](#references)

Especially the idea of weighted connections between neurons in a network allows for the creation of complex artificial neural networks that can learn from data, recognize patterns, and make predictions, making it a fundamental concept for artificial intelligence. For example, a deep neural network used for image recognition might have hundreds of thousands or even millions of neurons arranged in layers, with each neuron connected to many others through weighted connections. By adjusting these weights during training, the network can learn to recognize patterns in images, such as identifying faces or objects. While modern ANN’s are inspired by biological neural networks, it is important to note that they only loosely model the neurons in brains and do not completely mirror biological learning processes [[Mitchell 1997, p. 82]](#references). ANN’s for instance have fixed structures instead of being dynamic and do often rely on supervised learning [Section \ref{sec:ANN} \& \ref{sec:training}]. Furthermore, the actual process of adjusting the weights also differs but we will focus more on that in sections \ref{sec:gradient_descent} \& \ref{sec:backprop}. !TODO

<a id="praxis"></a>
## Handwritten Digit Recognition through Neural Networks

<a id="references"></a>
## References
