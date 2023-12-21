"use client";

import { useState } from "react";
import MessageWindow from "./message_window";
import InputForm from "./form";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost/message/";

type Message = {
  sender: string;
  content: string;
};

export default function Chat() {
  const [input, setInput] = useState("");
  const [cache, setCache] = useState(false);
  const [history, setHistory] = useState<Message[]>([]);

  function onChange(str: string) {
    setInput(str);
  }

  function onSend() {
    const body = {
      message: input,
      history: history.map((message) => {
        const type = message.sender === "User" ? "Human" : "AI";
        return {
          type: type,
          content: message.content,
        };
      }),
      cache: cache,
    };
    console.log(body);

    const newHistory = [
      ...history,
      {
        sender: "User",
        content: input,
      },
    ];

    setHistory(newHistory);

    fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    })
      .then((res) => res.json())
      .then((data) => {
        setHistory([
          ...newHistory,
          {
            sender: "AI",
            content: data.message,
          },
        ]);
        setInput("");
      });
  }

  return (
    <div className="w-1/2 h-screen">
      <div className="w-full p-2 flex">
        <div className="text-2xl w-1/2">LLM Caching Demo</div>
        <div className="ml-auto">
          <label>Cache</label>
          <select
            className="ml-2 bg-gray-800 rounded-md p-1"
            value={cache ? "true" : "false"}
            onChange={(e) => {
              setCache(e.target.value === "true");
            }}
          >
            <option value="true">Enabled</option>
            <option value="false">Disabled</option>
          </select>
        </div>
      </div>
      <div>
        {history.map((message, i) => {
          return (
            <div key={i}>
              <MessageWindow
                sender={message.sender}
                message={message.content}
              />
            </div>
          );
        })}
      </div>
      <div className="">
        <InputForm onChange={onChange} onSend={onSend} value={input} />
      </div>
    </div>
  );
}
