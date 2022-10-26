<?php
ini_set("memory_limit", "-1");

$start = time();
$options = getopt('f:ho:', ['file:', 'help', 'output:', 'vvv::', 'date::']);

echo file_get_contents('banner.txt') . PHP_EOL;

if (isset($options['h']) || isset($options['help'])) {
    exit();
}

if (empty($options['file'])) {
    output('Missing parameter: --file', '[ERROR]');
    exit();
}

if (empty($options['output'])) {
    output('Missing parameter: --output', '[ERROR]');
    exit();
}

if (!file_exists($options['file'])) {
    output('Missing word file.', '[ERROR]');
    exit();
}
$joiners = [
    '.',
    '_',
    '-',
    '=',
    '/',
    '\\',
    '#',
    '@',
    '~',
    ',',
    '|'
];

$substitutionArray = [
    's' => '$',
    'e' => '3',
    'l' => '1',
    'i' => '!',
    'a' => '@',
    't' => '7',
    'o' => '0'
];

$commonNumbers = [
    '1111',
    '!!!!',
    '2222',
    '3333',
    '4444',
    '5555',
    '6666',
    '7777',
    '8888',
    '9999',
    '0000',
    '1234',
    '!234',
    '432!',
    '432!',
    '123',
    '!23',
    '321',
    '32!',
    '12',
    '!2',
    '21',
    '2!',
    '1',
    '!',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0'
];

//=========LOAD FILE========================
output('Loading word list');
$wordList = [];
$handle = fopen($options['file'], "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {
        $line = str_replace('.', '', $line); // remove dots
        $line = str_replace(' ', '', $line); // remove spaces
        $line = str_replace("\t", '', $line); // remove tabs
        $line = str_replace("\n", '', $line); // remove new lines
        $line = str_replace("\r", '', $line); // remove carriage returns
        $wordList[] = $line;
    }
    fclose($handle);
    output('Word list loaded.');
}

// =============COMMON LISTS =================
output('Starting run');
$count = 0;
foreach ($wordList as $depth1) {
    $counter = 1;
    $prePayload = [];
    /// aaa
    /// AAA
    /// Aaa
    $prePayload[] = strtoupper($depth1);
    $prePayload[] = strtolower($depth1);
    $prePayload[] = ucfirst($depth1);
    foreach ($wordList as $depth2) {
        if ($depth2 == $depth1) {
            continue;
        }
        /// aaabbb
        /// aaaBBB
        /// AAAbbb
        /// AAABBB
        /// Aaabbb
        /// AaaBBB
        /// AaaBb
        $prePayload[] =  strtoupper($depth1) . strtoupper($depth2);
        $prePayload[] =  strtoupper($depth1) . strtolower($depth2);
        $prePayload[] = strtolower($depth1) . strtoupper($depth2);
        $prePayload[] = strtolower($depth1) . strtolower($depth2);
        $prePayload[] = ucfirst($depth1) . strtoupper($depth2);
        $prePayload[] = ucfirst($depth1) . strtolower($depth2);
        $prePayload[] = ucfirst($depth1). ucfirst($depth2);

       foreach ($joiners as $join) {
           /// aaa-bbb
           /// aaa-BBB
           /// AAA-bbb
           /// AAA-BBB
           /// Aaa-bbb
           /// Aaa-BBB
           /// Aaa-Bbb
           $prePayload[] = strtoupper($depth1). $join .  strtoupper($depth2);
           $prePayload[] = strtolower($depth1) . $join .  strtolower($depth2);
           $prePayload[] = strtoupper($depth1) . $join .  strtoupper($depth2);
           $prePayload[] = strtolower($depth1) . $join .  strtolower($depth2);
           $prePayload[] = strtoupper($depth1) . $join .  strtoupper($depth2);
           $prePayload[] = ucfirst($depth1). $join .  strtolower($depth2);
           $prePayload[] = ucfirst($depth1) . $join . ucfirst($depth2);
       }
    }

    // do a conversion for common charicter replace (substitutions).
   foreach ($prePayload as $node) {
       $workingNode = '';
       $nodeSplit = str_split($node);
       foreach ($nodeSplit as $letter) {
           if (isset($substitutionArray[$letter])) {
               $letter = $substitutionArray[$letter];
           }
           $workingNode .= $letter;
       }

       if ($node != $workingNode) {
           $prePayload[] = $workingNode;
       }
   }

    foreach ($prePayload as $word) {
        file_put_contents($options['output'], $word . PHP_EOL, FILE_APPEND | LOCK_EX);

        for($y=1900; $y <= date('Y'); $y++) {
            file_put_contents($options['output'], $word . $y . PHP_EOL, FILE_APPEND | LOCK_EX);
            $count++;
            counterShow($count);
        }

        foreach ($commonNumbers as $node) {
            file_put_contents($options['output'], $word . $node . PHP_EOL, FILE_APPEND | LOCK_EX);
            $count++;
            counterShow($count);
        }
    }
    output('[' . $depth1 . '] word interation complete.');
    unset($prePayload);
}
output('Script complete ' . (time() - $start) . ' seconds');

/**
 * Outputs something on the screen, only in verbose mode though unless status is error.
 *
 * @param $message
 * @param $status
 * @return void
 */
function output($message, $status = '[INFO]') {
    global $options;

    if (isset($options['vvv']) || $status == '[ERROR]') {
        echo $status . ' ' . $message . PHP_EOL;
    }
}

/**
 * Counter show with flush.
 * @param $count
 * @return void
 */
function counterShow($count) {
    echo "\rProcessed: ";
    echo "$count  ";
    flush();
}