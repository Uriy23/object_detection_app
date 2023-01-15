class ShowForm {
  constructor() {
    this.ctx = this.canvasCtx
    this.waitForImageLoad()
  }

  showBoxes() {
    this.imageBoxes.forEach((box, index) => {
      const boxLabel = this.imageBoxLabels[index]
      this.renderBox(box)
      this.renderLabel(box, boxLabel)
    })
  }

  renderLabel(pythonBox, labelText) {
    const [boxLeft, boxTop, _boxWidth, _boxHeight] = this.pythonBoxCoordsToCanvas(pythonBox)
    const labelBox = document.createElement('div')
    labelBox.classList.add('image-box--label')
    labelBox.innerText = labelText
    labelBox.style.top = boxTop
    labelBox.style.left = boxLeft
    this.insideWrapper.appendChild(labelBox)
  }

  renderBox(pythonBox) {
    const [boxLeft, boxTop, boxWidth, boxHeight] = this.pythonBoxCoordsToCanvas(pythonBox)
    this.ctx.strokeRect(boxLeft, boxTop, boxWidth, boxHeight)
  }

  pythonBoxCoordsToCanvas(pythonBox) {
    let [boxLeft, boxTop, boxRight, boxBottom] = pythonBox
    boxLeft *= this.imageScale
    boxTop *= this.imageScale
    const boxWidth = boxRight * this.imageScale - boxLeft
    const boxHeight = boxBottom * this.imageScale - boxTop
    return [boxLeft, boxTop, boxWidth, boxHeight]
  }

  waitForImageLoad() {
    let img = document.querySelector('#target-image')
    img.onload = () => {
      this.imageRecognized = img
      this.imageScale = this.imageRecognized.offsetWidth / this.imageRecognized.naturalWidth
      this.showBoxes()
    }
  }

  get canvasCtx() {
    const canvas = document.querySelector('.covering-canvas')
    const ctx = canvas.getContext('2d')
    ctx.lineWidth = 1
    ctx.strokeStyle = 'red'
    return ctx
  }

  get imageBoxes() {
    const image = this.imageRecognized
    return this.readDataAttribute(image, 'data-list-box')
  }

  get imageBoxLabels() {
    const image = this.imageRecognized
    return this.readDataAttribute(image, 'data-list-name')
  }

  readDataAttribute(element, attributeName) {
    if (element === null) return []
    const dataAttribute = element.getAttribute(attributeName)
    if (dataAttribute === '') return []

    return JSON.parse(dataAttribute)
  }

  get insideWrapper() {
    return document.querySelector('.inside-wrapper')
  }
}

init = () => {
  showForm = new ShowForm()
}

document.addEventListener('DOMContentLoaded', init)
