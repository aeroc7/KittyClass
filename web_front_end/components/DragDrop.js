export default function DragDrop({ onResponse }) {
    const uploadImage = async (img) => {
        try {
            const DOMAIN = `http://${process.env.NEXT_PUBLIC_SERVER_IP}:5000`
            const PATH = '/upload.js'

            let res = await fetch(DOMAIN + PATH, {
                method: 'POST',
                body: img,
            });

            let text_data = await res.text()
            onResponse(text_data.toString());
        } catch (err) {
            console.log(err);
            onResponse(err.toString());
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
            <form onSubmit={handleImage} className="flex flex-col sm:flex-row">
                <input type="file" id="file" accept=".png,.jpg,.webp" className="bg-background border-2 border-text text-text py-4 rounded-lg px-2 text-right font-roboto text-md" />
                <button type="submit" className="flex bg-background border-2 border-text text-text sm:ml-2 mt-2 sm:mt-0 px-2 py-4 rounded-lg font-roboto text-md justify-center items-center">SUBMIT</button>
            </form>
        </div>
    )
}