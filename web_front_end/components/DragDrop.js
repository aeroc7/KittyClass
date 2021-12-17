export default function DragDrop() {
    const handleImage = async (e) => {
        e.preventDefault();

        var image = document.getElementById("file").files[0];
        var formData = new FormData();

        formData.append('image', image);

        try {
            await fetch('upload.js', {
                method: 'POST',
                body: formData
            });
        } catch (err) {
            console.log(err);
        }
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