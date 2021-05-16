# MQTT topic overview

The main topic level is `quantum_cryptography`. All MQTT messages in this project start with it.
It has two sub-topics, which in turn have more granular topics:

* `clasiscal_channel`
  * All communication that is to happen over the classical channel according to the BB84 protocol.
* `quantum_channel`
  * For the simulation of the quantum channel (to use the project without hardware).
* `debug_channel`
  * A debug channel that can be used for arbitrary log messages.
  * **This data may not be used in the BB84 scheme.**

## the classical channel

* `alice`
  * `laser`
    * msg: `on`
    * msg: `off`
* `bob`
  * `light-sensor`
    * msg: `on`
    * msg: `off`

As an example: if Alice turns the laser on to send a bit she will send
the message-payload **`on`** over the channel `quantum_cryptography/classical_channel/alice/laser`.

**Do not use a leading `/`, it introduces an uneccessary empty level.**

