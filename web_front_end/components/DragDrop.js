export default function DragDrop() {
    const uploadImage = async (img) => {
        try {
            const DOMAIN = 'http://localhost:5000'
            const PATH = '/upload.js'

            await fetch(DOMAIN + PATH, {
                method: 'POST',
                body: img,
            });
        } catch (err) {
            console.log(err);
        }
    }

    const handleImage = (e) => {
        e.preventDefault();

        var image = document.getElementById("file").files[0];
        const reader = new FileReader();

        reader.addEventListener('load', () => {
            var img_raw = reader.result;
            uploadImage(img_raw);
        });

        reader.readAsDataURL(image);
    }

    return (
        <div className="w-full h-[85%] flex justify-center items-center" id="prev">
            <form onSubmit={handleImage}>
                <input type="file" id="file" accept=".png,.jpg,.webp" className="bg-text py-2 rounded-lg px-2" />
                <button type="submit" className="bg-text ml-5 px-2 py-2 rounded-lg">ENTER</button>
            </form>
        </div>
    )
}