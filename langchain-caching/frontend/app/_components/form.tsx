"use client";

type Props = {
    value?: string;
    onChange?: (input: string) => void;
    onSend?: () => void;
}


export default function Form(props: Props) {
    function onChange(event: React.ChangeEvent<HTMLInputElement>) {
        if (props.onChange){
            props.onChange(event.target.value);
        }
    };

    return <div className="rounded-lg border border-gray-600 bg-black p-2 w-full">
        <input className="bg-black focus:outline-none text-gray-400 w-11/12" placeholder="Message..." onChange={onChange} value={props.value}/>
        <button className="bg-gray-700 text-gray-400 rounded-lg p-1 hover:bg-gray-900" onClick={props.onSend}>Send</button>
    </div>
}