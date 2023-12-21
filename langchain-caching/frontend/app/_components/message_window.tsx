"use client";

type Props = {
    sender: string;
    message: string;
}

export default function MessageWindow(props: Props) {
    return <div className="w-full">
        <div className="font-bold">
            {props.sender}
        </div>
        <div>
            {props.message}
        </div>
    </div>
}