Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
async function startProgram() {
        setMainLed({ r: 255, g: 0, b: 19 });
        await roll(0, 27, 2);
        setMainLed({ r: 255, g: 171, b: 0 });
        await roll(180, -27, 4);
        setMainLed({ r: 238, g: 255, b: 0 });
        await roll(0, 26, 2);
        setMainLed({ r: 224, g: 0, b: 255 });
        await roll(270, 26, 4);
        setMainLed({ r: 0, g: 15, b: 255 });
        await roll(90, 27, 2);
        setMainLed({ r: 0, g: 255, b: 14 });
        await speak('Pretty good right?', true);
        stopRoll();
}
